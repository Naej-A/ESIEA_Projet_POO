import sample.cards.Card as Card
class CardHPBoost(Card):

    def __init__(self, name, race, gamePhase, level, attack, maxHealthPoint, description, HPBoost):
        self.HPBoost = HPBoost
        super().__init__(name, race, gamePhase, level, attack, maxHealthPoint, description)

    def doEffect(self, game, targetDeck):
        """
        ajoute le boost d'HP de la carte
        :param game: the currently running game
        :param targetDeck: the deck to boost Card's hp
        :return: None
        """
        super().doEffect(game, targetDeck)
        if game.gamePhase.name == self.gamePhase.name:
            for card in targetDeck.listCard:
                if card.race == self.race:
                    card.currentHealthPoint += self.HPBoost
