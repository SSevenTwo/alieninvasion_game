import json

def save_score(stats):
    score = stats.highscore
    filename = "highscore.json"
    
    with open(filename, "w") as hsfile:
        json.dump(score, hsfile)
        
    print("Score saved.")
        
def load_score(stats,scoreboard):
    filename = "highscore.json"
    
    try:
        with open(filename) as hsfile:
            stats.highscore = json.load(hsfile)
            scoreboard.prep_highscore()
    except FileNotFoundError:
        pass

