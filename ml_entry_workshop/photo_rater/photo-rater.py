import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QComboBox,
    QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import os


from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel

class GenderSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_gender = None  # Store selection

        self.setWindowTitle("Select Gender Category")
        layout = QVBoxLayout()

        label = QLabel("Would you prefer 'Men' or 'Women'?", self)
        layout.addWidget(label)

        self.men_button = QPushButton("Men", self)
        self.men_button.clicked.connect(lambda: self.select_gender("Men"))
        layout.addWidget(self.men_button)

        self.women_button = QPushButton("Women", self)
        self.women_button.clicked.connect(lambda: self.select_gender("Women"))
        layout.addWidget(self.women_button)

        self.setLayout(layout)

    def select_gender(self, gender):
        self.selected_gender = gender
        self.accept()  # Close the dialog


class PhotoRater(QWidget):
    def __init__(self, photo_dir, output_file_name):
        super().__init__()
        self.setWindowTitle("Photo Rater")
        self.photo_dir = photo_dir
        self.photos = [f for f in os.listdir(photo_dir) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
        self.output_file_name = output_file_name
        self.current_index = 0
        self.ratings = {}

        # Image display
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Buttons
        self.like_button = QPushButton("👍 Like", self)
        self.dislike_button = QPushButton("👎 Dislike", self)
        self.like_button.clicked.connect(lambda: self.rate_photo(True))
        self.dislike_button.clicked.connect(lambda: self.rate_photo(False))

        # Progress Counter
        self.progress_label = QLabel(self)
        self.progress_label.setAlignment(Qt.AlignCenter)

        # Finish Button
        self.finish_button = QPushButton("Finish", self)
        self.finish_button.clicked.connect(self.finish_early)

        # Layout setup
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.progress_label)  # Counter at the top
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.like_button)
        self.layout.addWidget(self.dislike_button)
        self.layout.addWidget(self.finish_button)  # Finish button at the bottom

        self.setLayout(self.layout)

        # Ensure correct initial state
        self.in_summary_mode = False
        self.update_progress()  # Show initial progress before first photo
        self.load_photo()

    def show_summary(self):
        self.setWindowTitle("Summary")

        # Clear the current layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Create a table widget
        table = QTableWidget()
        table.setRowCount(len(self.ratings))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Photo Index", "Thumbnail", "Rating"])

        # Populate the table with data
        for row, (photo, liked) in enumerate(self.ratings.items()):
            # Photo index
            table.setItem(row, 0, QTableWidgetItem(str(row + 1)))

            # Thumbnail
            pixmap = QPixmap(os.path.join(self.photo_dir, photo)).scaled(100, 100, Qt.KeepAspectRatio,
                                                                         Qt.SmoothTransformation)
            thumbnail_item = QLabel()
            thumbnail_item.setPixmap(pixmap)
            table.setCellWidget(row, 1, thumbnail_item)

            # Editable rating dropdown
            rating_dropdown = QComboBox()
            rating_dropdown.addItems(["Liked", "Disliked"])
            rating_dropdown.setCurrentText("Liked" if liked else "Disliked")
            rating_dropdown.currentTextChanged.connect(lambda value, p=photo: self.update_rating(p, value))
            table.setCellWidget(row, 2, rating_dropdown)

        # Adjust table appearance
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Add save button
        self.save_button = QPushButton("💾 Save Ratings", self)
        self.save_button.clicked.connect(self.save_ratings)

        # Add widgets to layout
        self.layout.addWidget(table)
        self.layout.addWidget(self.save_button)
        self.in_summary_mode = True

    def update_rating(self, photo, value):
        """Update the rating in the dictionary based on dropdown change."""
        self.ratings[photo] = (value == "Liked")

    def load_photo(self):
        if self.current_index < len(self.photos):
            pixmap = QPixmap(os.path.join(self.photo_dir, self.photos[self.current_index]))
            # Scale the photo to a consistent size while keeping the aspect ratio
            scaled_pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
        else:
            self.show_summary()

    def rate_photo(self, liked):
        if self.current_index < len(self.photos):
            self.ratings[self.photos[self.current_index]] = liked
            self.current_index += 1
            self.update_progress()

            if self.current_index < len(self.photos):
                self.load_photo()
            else:
                self.show_summary()

    def update_progress(self):
        self.progress_label.setText(f"Photos Labeled: {len(self.ratings)} / {len(self.photos)}")


    def keyPressEvent(self, event):
        if self.in_summary_mode:
            return # do nothing
        if event.key() == Qt.Key_Right:
            self.rate_photo(True)
        elif event.key() == Qt.Key_Left:
            self.rate_photo(False)


    def organize_photos_by_rating(self, photo_dir, ratings_file):
        # Find the root directory (assumes 'my_workshop' is the project root)
        root_dir = Path(__file__).resolve().parent.parent  # Moves up from 'photo_rater' to 'my_workshop'

        # Set the correct dataset directory
        output_dir = os.path.join(root_dir,"data", "dataset")

        # Ensure the dataset directories exist
        like_dir = os.path.join(output_dir, "1")
        dislike_dir = os.path.join(output_dir, "0")
        os.makedirs(like_dir, exist_ok=True)
        os.makedirs(dislike_dir, exist_ok=True)

        # Load ratings from JSON
        with open(ratings_file, "r") as f:
            ratings = json.load(f)

        # Move photos based on rating
        for photo, rating in ratings.items():
            src_path = os.path.join(photo_dir, photo)
            if not os.path.exists(src_path):
                print(f"Warning: {src_path} not found, skipping...")
                continue

            dest_dir = like_dir if rating['rating'] == 1 else dislike_dir
            dest_path = os.path.join(dest_dir, photo)

            shutil.copy2(src_path, dest_path)  # Use copy2 to retain metadata
            print(f"Copied {photo} -> {dest_path}")

    def save_ratings(self):
        root_dir = Path(__file__).resolve().parent.parent  # Moves up from 'photo_rater' to 'my_workshop'

        # Set the correct dataset directory
        output_dir = os.path.join(root_dir, "data")

        save_path = os.path.join(output_dir, self.output_file_name)
        msg = QMessageBox()
        msg.setWindowTitle("Save and Exit")
        msg.setText(f"This will save the results to '{save_path}' and exit.")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)

        msg.button(QMessageBox.Yes).setShortcut(Qt.Key_Return)
        msg.button(QMessageBox.No).setShortcut(Qt.Key_Delete)

        response = msg.exec_()
        if response == QMessageBox.Yes:
            try:
                ratings_with_timestamp = {
                    photo: {
                        "rating": int(liked),
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    for photo, liked in self.ratings.items()
                }
                with open(save_path, 'w') as f:
                    json.dump(ratings_with_timestamp, f, indent=2)
                # Use QTimer to safely quit after the dialog closes
                from PyQt5.QtCore import QTimer
                QTimer.singleShot(0, QApplication.quit)

                # Now, organize photos based on ratings
                self.organize_photos_by_rating(photo_dir=self.photo_dir, ratings_file=save_path)  # Pass save_path instead
                print("Photos successfully organized!")

            except Exception as e:
                error_msg = QMessageBox()
                error_msg.setWindowTitle("Error")
                error_msg.setText(f"Failed to save: {str(e)}")
                error_msg.exec_()

    def finish_early(self):
        self.show_summary()  # Jump to summary immediately


def run_app():
    app = QApplication([])

    # Show gender selection dialog
    dialog = GenderSelectionDialog()
    if dialog.exec_() == QDialog.Accepted:
        selected_gender = dialog.selected_gender
        if selected_gender:
            photo_dir = os.path.join("photos", selected_gender)  # Adjust path
            print(f"Selected directory: {photo_dir}")

            # Start the photo rater with selected directory
            rater = PhotoRater(photo_dir, "ratings.json")
            rater.show()
            app.exec_()


if __name__ == "__main__":
    run_app()