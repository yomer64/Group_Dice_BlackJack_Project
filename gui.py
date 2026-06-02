import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QSpinBox
)
from PyQt5.QtCore import Qt
from game import Player
from dice import player_hit, dealer_hit, stand_player, stand_dealer
from PyQt5.QtGui import QPixmap

house_busts_player_response = [
    "The Dealer: \n Sorry bud better luck next time",
]

#intro
class BlackjackApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diced Blackjack")
        self.setGeometry(200, 200, 400, 300)

        self.title_label = QLabel("Welcome to Diced Blackjack!")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold;")

      

        # Create image label
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(QPixmap("diceimg.png").scaled(120, 120, Qt.KeepAspectRatio))
        

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")

        self.start_button = QPushButton("Start Game")
        self.start_button.clicked.connect(self.start_game)

        self.exit_button = QPushButton("Exit Game")
        self.exit_button.clicked.connect(self.close_app)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.image_label) 
        layout.addWidget(self.name_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.exit_button)
        layout.addStretch()
        self.setLayout(layout)

    def start_game(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Missing Name", "Please enter your name!")
            return

        self.player = Player(name)
        self.game_window = GameWindow(self.player)
        self.game_window.show()
        self.close()

    def close_app(self):
        user_choice = QMessageBox.question(
            self,
            "Exit Game",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if user_choice == QMessageBox.Yes:
            QApplication.quit()

#bet system
class GameWindow(QWidget):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.money = 1000
        self.sub_total_score = 0
        self.round = 1
        self.bet_amount = 0

        self.setWindowTitle(f"Diced Blackjack - {self.player.name}")
        self.setGeometry(250, 250, 500, 400)
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(
            QPixmap("dealerimg.png").scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        self.info_label = QLabel(f"Hello {self.player.name}! You have ${self.money}")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.score_label = QLabel("Your current score: 0")
        self.bet_label = QLabel("Place your bet:")

        self.bet_input = QSpinBox()
        self.bet_input.setRange(1, self.money)
        self.bet_input.setValue(1)

        self.bet_button = QPushButton("Place Bet")
        self.bet_button.clicked.connect(self.place_bet)

        self.hit_button = QPushButton("Hit (Roll 2 Dice)")
        self.hit_button.clicked.connect(self.hit)
        self.hit_button.setEnabled(False)

        self.stand_button = QPushButton("Stand")
        self.stand_button.clicked.connect(self.stand)
        self.stand_button.setEnabled(False)

        self.exit_button = QPushButton("Exit Game")
        self.exit_button.clicked.connect(self.close_game)

 
        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.score_label)
        layout.addWidget(self.bet_label)
        layout.addWidget(self.bet_input)
        layout.addWidget(self.bet_button)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.hit_button)
        buttons_layout.addWidget(self.stand_button)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.exit_button)
        self.setLayout(layout)

    #betting action
    def place_bet(self):
        bet = self.bet_input.value()
        if bet > self.money:
            QMessageBox.warning(self, "Invalid Bet", f"You can't bet more than ${self.money}")
            return
        self.bet_amount = bet
        self.money -= bet
        self.info_label.setText(f"Bet placed: ${self.bet_amount}. Money left: ${self.money}")
        self.bet_button.setEnabled(False)
        self.bet_input.setEnabled(False)
        self.hit_button.setEnabled(True)
        self.stand_button.setEnabled(True)
        self.roll_first()
    #hiting/rolling
    def roll_first(self):

        roll = player_hit()
        self.sub_total_score += roll
        self.score_label.setText(f"Your total score: {self.sub_total_score}")
        if self.sub_total_score == 21:
            QMessageBox.information(self, "Blackjack!", "You hit 21! You win 4x your bet!")
            self.money += self.bet_amount * 4
            stand_player(self.sub_total_score)
            self.end_round()
        else:
            self.info_label.setText(f"Your current score: {self.sub_total_score}. Hit or Stand?")

    def hit(self):
        roll = player_hit()
        self.sub_total_score += roll
        self.score_label.setText(f"Your total score: {self.sub_total_score}")
        if self.sub_total_score > 21:
            response = random.choice(house_busts_player_response)
            QMessageBox.information(self, "Busted!", f"{response}\nYou busted with {self.sub_total_score}")
            stand_player(self.sub_total_score)
            self.end_round()
        elif self.sub_total_score == 21:
            QMessageBox.information(self, "Blackjack!", "You hit 21! You win 4x your bet!")
            self.money += self.bet_amount * 4
            stand_player(self.sub_total_score)
            self.end_round()
#standing, checking scroes, and checking for bust.
    def stand(self):
        stand_player(self.sub_total_score)
        dealer_total = 0
        dealer_rolls = []

        while dealer_total < 18:
            roll = dealer_hit()
            dealer_total += roll
            dealer_rolls.append(roll)
        stand_dealer(dealer_total)

        if dealer_total > 21 or self.sub_total_score > dealer_total:
            QMessageBox.information(self, "You Win!", f"Dealer rolled {dealer_rolls} (total {dealer_total}). You win!")
            self.money += self.bet_amount * 2
        else:
            response = random.choice(house_busts_player_response)
            QMessageBox.information(self, "Dealer Wins!", f"Dealer rolled {dealer_rolls} (total {dealer_total}). {response}")

        self.end_round()
#
    def end_round(self):
        self.sub_total_score = 0
        self.bet_amount = 0
        if self.money <= 0:
            rebuy = QMessageBox.question(
                self, "Out of Money", "Do you want to rebuy for $1000?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if rebuy == QMessageBox.Yes:
                self.money = 1000
            else:
                self.close()
                return


        self.info_label.setText(f"Money: ${self.money}")
        self.score_label.setText("Your current score: 0")
        self.bet_input.setMaximum(self.money)
        self.bet_input.setValue(1)
        self.bet_input.setEnabled(True)
        self.bet_button.setEnabled(True)
        self.hit_button.setEnabled(False)
        self.stand_button.setEnabled(False)
#quits the app
    def close_game(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlackjackApp()
    window.show()
    sys.exit(app.exec_())
