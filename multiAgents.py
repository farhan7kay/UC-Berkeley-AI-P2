# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        foods = []
        ghosts = []

        for x in newFood.asList():
            foods.append(manhattanDistance(newPos, x))

        # closest and the furthest food (if food left)
        if (newFood.asList() != []):
            closestFood = min(foods)
            furthestFood = max(foods)
        else:
            return successorGameState.getScore()

        # closest ghost 
        for ghost in newGhostStates:
            ghosts.append(manhattanDistance(newPos,ghost.getPosition()))

        if (ghosts != []):
           minGhostDist = min(ghosts)


        # If there is only 1 food left then furthestFood == closestFood
        if len(newFood.asList()) == 1:
            score = minGhostDist - closestFood
        else:
            score = minGhostDist - (furthestFood + closestFood)

        return successorGameState.getScore() + score

      
def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        def max(gameState,depth):
            if len(gameState.getLegalActions(0))== 0 or gameState.isWin() or gameState.isLose() or depth == self.depth:             
                return(self.evaluationFunction(gameState), None)
            w = -(float("inf"))                                                                              
            Act = None
            for action in gameState.getLegalActions(0):                                                                          
                sucsValue = min(gameState.generateSuccessor(0,action), 1, depth)                          
                sucsValue = sucsValue[0]                                                                      
                if(sucsValue > w):                                                                            
                    w, Act = sucsValue, action
            return(w, Act)

        def min(gameState,agentID,depth):
            if len(gameState.getLegalActions(agentID)) == 0:
                return(self.evaluationFunction(gameState), None)
            l=float("inf")                                                                                  
            Act = None
            for action in gameState.getLegalActions(agentID):
                if(agentID == gameState.getNumAgents() -1):
                    sucsValue = max(gameState.generateSuccessor(agentID, action), depth + 1)
                else:
                    sucsValue = min(gameState.generateSuccessor(agentID, action), agentID + 1, depth)        
                sucsValue = sucsValue[0]
                if(sucsValue < l):
                    l, Act = sucsValue, action
            return(l, Act)
        
        return max(gameState,0)[1]                                                                                   



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        Infinity = float('inf')

        def minValue(state, agentIndex, depth, a, b):
            if not state.getLegalActions(agentIndex):
                return self.evaluationFunction(state)

            v = Infinity
            for action in state.getLegalActions(agentIndex):

                # last ghost?
                if agentIndex == state.getNumAgents() - 1:
                    newV = maxValue(state.generateSuccessor(agentIndex, action), depth, a, b)
                else:
                    newV = minValue(state.generateSuccessor(agentIndex, action), agentIndex + 1, depth, a, b)

                v = min(v, newV)
                if v < a:
                    return v
                b = min(b, v)
            return v

        def maxValue(state, depth, a, b):
            legalActions = state.getLegalActions(0)
            if not legalActions or depth == self.depth:
                return self.evaluationFunction(state)

            v = -Infinity
            # enable second play prune
            if depth == 0:
                bestAction = legalActions[0]
            for action in legalActions:
                newState = state.generateSuccessor(0, action)
                newV = minValue(newState, 0 + 1, depth + 1, a, b)
                if newV > v:
                    v = newV
                    if depth == 0:
                        bestAction = action
                if v > b:
                    return v
                a = max(a, v)

            if depth == 0:
                return bestAction
            return v
 
        return maxValue(gameState, 0, -Infinity, Infinity)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        numAgent = gameState.getNumAgents()
        ActionScore = []

        def rmStop(List):
          return [x for x in List if x != 'Stop']

        def expectMinimax(s, iterCount):
          if iterCount >= self.depth*numAgent or s.isWin() or s.isLose():
            return self.evaluationFunction(s)
          if iterCount%numAgent != 0: #min ghost
            successorScore = []
            for a in rmStop(s.getLegalActions(iterCount%numAgent)):
              result = expectMinimax(s.generateSuccessor(iterCount%numAgent,a), iterCount+1)
              successorScore.append(result)
            averageScore = sum([ float(x)/len(successorScore) for x in successorScore])
            return averageScore
          else: # max pacman
            result = -1e10
            for a in rmStop(s.getLegalActions(iterCount%numAgent)):
              result = max(result, expectMinimax(s.generateSuccessor(iterCount%numAgent,a), iterCount+1))
              if iterCount == 0:
                ActionScore.append(result)
            return result
          
        result = expectMinimax(gameState, 0)
        return rmStop(gameState.getLegalActions(0))[ActionScore.index(max(ActionScore))]


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"                                                                                                

    if currentGameState.isWin():
        return float("inf")
    if currentGameState.isLose():
        return float("-inf")

    foodDistList = []
    for food in currentGameState.getFood().asList():
        foodDistList += [util.manhattanDistance(food,currentGameState.getPacmanPosition()   )]
    minFDist = min(foodDistList)                                                                              
    GhDistList = []                                                                                         
    ScGhDistList = []                                                                                         
    for ghost in currentGameState.getGhostStates():                                                                                    
        if ghost.scaredTimer == 0:
            GhDistList += [util.manhattanDistance(currentGameState.getPacmanPosition(), ghost.getPosition())]
        elif ghost.scaredTimer > 0:
            ScGhDistList += [util.manhattanDistance(currentGameState.getPacmanPosition(), ghost.getPosition())]
    minGhDist = -1
    if len(GhDistList) > 0:
        minGhDist=min(GhDistList)  

    Food = currentGameState.getFood()
    Capsules = currentGameState.getCapsules()                                                                          
    minScGhDist = -1                                                                                            
    if len(ScGhDistList) > 0:
        minScGhDist = min(ScGhDistList)
    score = scoreEvaluationFunction(currentGameState)
    score -= 1.5 * minFDist + 2 * (1.0/minGhDist) + 2 * minScGhDist + 20 * len(Capsules) + 4 * len(Food.asList())
    return score

# Abbreviation
better = betterEvaluationFunction
