# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    else:
        open = util.Stack()
        open.push((start, [start], []))

    # check if open is empty
    while not open.isEmpty():
        state, path, action = open.pop()
        successors = problem.getSuccessors(state)

        for state, next_action, cost in successors:
            # do the path checking
            if state not in path:
                start = state
                new_action = action + [next_action]
                new_path = path + [state]
                open.push((state, new_path, new_action))

        if problem.isGoalState(start):
            return new_action

    return new_action
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    else:
        open = util.Queue()
        open.push((start, [], 0))
    # set the initial variable of checking info
    checking = {start: 0}

    # check if open is empty
    while not open.isEmpty():
        state, action, curr_cost = open.pop()
        if problem.isGoalState(state):
            return action

        # do the full cycle checking
        if curr_cost <= checking[state]:
            successors = problem.getSuccessors(state)
            for state, next_action, cost in successors:
                new_action = action + [next_action]
                new_cost = problem.getCostOfActions(new_action)
                if state not in checking or new_cost < checking[state]:
                    open.push((state, new_action, new_cost))
                    checking[state] = new_cost

    return action
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    else:
        open = util.PriorityQueue()
        open.push((start, [], 0), 0)

    checking = {start: 0}

    while not open.isEmpty():
        state, action, curr_cost = open.pop()

        if problem.isGoalState(state):
            return action
        # do the full cycle checking
        if curr_cost <= checking[state]:
            successors = problem.getSuccessors(state)
            for next, next_action, cost in successors:
                new_action = action + [next_action]
                new_cost = problem.getCostOfActions(new_action)
                if next not in checking or new_cost < checking[next]:
                    open.push((next, new_action, new_cost), new_cost)
                    checking[next] = new_cost

    return action
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    else:
        open = util.PriorityQueue()
        open.push((start, [], heuristic(start, problem)), nullHeuristic(start, problem))

    checking = {start: heuristic(start, problem)}

    while not open.isEmpty():
        state, action, cost = open.pop()
        
        if cost <= checking[state]:
            if problem.isGoalState(state):
                return action
            successors = problem.getSuccessors(state)
            for next, next_action, cost in successors:
                new_action = action + [next_action]
                moving_cost = problem.getCostOfActions(new_action)
                new_cost = moving_cost + heuristic(next, problem)
                if next not in checking or new_cost < checking[next]:
                    open.push((next, new_action, new_cost), new_cost)
                    checking[next] = new_cost
    return action
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
