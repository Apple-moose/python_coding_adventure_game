situations = {
    "start": "So, here you are again, laptop in hands. You start to WRITE CODE",
    "first options": "Your think that it's going to work this time, but you hit this \
damn meanError again...What is it going to be this time? \
You turn to STACK OVERFLOW, talk to the DUCK or walk to the FRIDGE? (you can always call a FRIEND for a quick fix)",
    "stack overflow": "You turn to your most trusted friend on the web. There are tons of solutions \
exposed on many pages but, somehow, it's all gibberish, nothing is usable...Be honest: you start building internal FRUSTRATION or \
you calmly turn to other ressources and STUDY some more?",
    "duck": "y",
    "fridge": "y",
    "friend": "After a couple of calls, finally someone picks up and helps you solve the issue. \
Smart friend. Always there for you. Now, on to the next issue...(write code)",
    "frustration": "y",
    "study": "Zen as a bonsai, you turn to other websites and try not to deviate from the path too much...",
    "study2": "You take a couple of minutes to ponder your options: you can always let it go and SLEEP ON IT, \
see what tomorrow brings. Also you can OBSESS and stay on course until you make the code work or, \
look inward and see if you are not, in fact, building some kind of FRUSTRATION",
    "obsess": "OK, you got this. Knife between your teeth you try to make it work using the sheer power of Will",
    "abandon": "y",
    "x": "y",
    "x": "y",
    "x": "y",
    "x": "y",
    "x": "y",
    "x": "y",
    "x": "y",
    "profile": "y",
    "success": "You did it! WOW!.... ....does it matter how? Let's check your PROFILE together??",

  
}
 
solutions = {
    "start": {"write code": "first options"},
    "first options": {"stack overflow": "stack overflow", "duck": "duck", "fridge": "fridge", "friend": "friend"},
    "stack overflow": {"frustration": "frustration", "friend": "friend"},
    "study": {"duck": "duck", "fridge": "fridge", "frustration": "frustration"},
    "friend": {"write code": "first options", "z": "z1", "a": "a1"},
    "frustration": {"y": "y1", "z": "z1", "a": "a1"},
    "obsess": {"abandon": "abandon", "s": "s", "a": "a1"},
    "abandon": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "x": {"y": "y1", "z": "z1", "a": "a1"},
    "profile": {"y": "y1", "z": "z1", "a": "a1"},
    "sucess": {"profile": "profile", "z": "z1", "a": "a1"},
}

analisis ={
    "obsessed":"Very confident in your own capacities. But, you are tired, exhausted...and after a while, so is everyone around you. Not sure you can do the same tomorrow...\
It kinds of beg the question: Wouldn't it be more productive to take a breather sometimes?"


}