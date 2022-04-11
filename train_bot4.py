from Players.DRLModel import DRLModel

# ----------------------------------------------
# Main program to train the bot4 DRL model
# ----------------------------------------------
if __name__ == '__main__':
    n_episodes = 10000
    model_filename = "NN/bot4_1e4.nn"

    model = DRLModel()                  # Create the drl model
    model.train(n_episodes)             # Train n_episodes episodes
    model.save_to_disk(model_filename)  # Save to disk


