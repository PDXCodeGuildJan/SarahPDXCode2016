""" A computer version the game of Mastermind """

__author__ = "Sarah Fellows"

import master_model
import master_view
# alternative to import every class: from master_view import show_rules, show_player_peg, show_key_peg, promt_user, win
#maybe use later on when we have all the classes identified 


class MasterMind:
    """ Defines the class MasterMind in the conroller function (logic)."""

        def play_game():
            """ Has the user play the game of MasterMind. Loops through until 
                the user wins or looses"""
            pass

        def check_win():
            """ Defines the method check_win that will check if the player's 
                choice matches the games randomized goal"""
            pass

        def eval_peg_color():
            """Evaluates whether the player's peg colors matches any of the 
                computers colors"""
            pass

        def eval_peg_position():
            """Evaltues whether the player's matched colors also match any 
                positions from the comp generated goal"""
            pass
            

        def generate_goal():

            goal = []

            for x in range(4):

                player_peg = master_model.PlayerPeg(random.choice(master_model.MasterModel.peg_colors))

                goal.append(player_peg)

                return master_model.MasterModel.goal