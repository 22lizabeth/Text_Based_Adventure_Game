class Effects:

    def __init__(self):
        self.worshipEffect = "inactive"

    def worship(self):
        if self.worshipEffect == "inactive":
            print("\nYou worship quietly and calmly at the Shrine of Memories, and you feel its power begin to envelop you." \
            + " You see a vision of a spiritual form of yourself, older and wiser, possibly even new and reborn. You see that self " \
            + "merge with your current self and the vision dissipates. You feel a sense of peace that even if you were to die on this "\
            + "adventure, everything would turn out all right.")
            self.worshipEffect = "active"
        elif self.worshipEffect == "active":
            print("\nYou have recently worshipped at this shrine and received it's gift. You continue to feel the same peace you felt when you " \
            +"worshipped the first time. If something terrible were to happen to you, you feel protected and safe.")
        else:
            print("\nYou have already experienced the blessing and power of this shrine. Though you may continue to worship at it and feel " \
            + "at peace, you also know that this shrine has already offered you all the power it had to give")

