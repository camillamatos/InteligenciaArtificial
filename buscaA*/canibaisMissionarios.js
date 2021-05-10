 //m c b m c b 
const inicio = {
 children: [],
 distanceInicial: 0,
 state: [3,3,1,0,0,0]
}

const final = {
 parent: null,
 children: [],
 state: [0,0,0,3,3,1]
}

const possibleStates = [
  [1,1],
  [0,1],
  [1,0],
  [2,0],
  [0,2],
]

let visitedNode = []
let result

function transform(e){
  if(e == 0){
    return '000'
  }else if(e == 1) {
    return '001'
  }else if(e == 2) {
    return '011'
  }else if(e == 3) {
    return '111'
  }
}

function hammingDistance(a, b) {
  let distance = 0

  const newA = `${transform(a[0]) + transform(a[1]) + transform(a[3]) + transform(a[4])}`
  const newB = `${transform(b[0]) + transform(b[1]) + transform(b[3]) + transform(b[4])}`

  for (let i = 0; i < newA.length; i += 1) {
    if (newA[i] !== newB[i]) {
      distance += 1
    }
  }
 
  return distance;
}

function validState(currentState){ //verificar se o estado é valido e se ainda não foi percorrido
  if(visitedNode.includes(currentState.toString()))return false

  if((currentState[0] < currentState[1] && currentState[0] != 0) || (currentState[3] < currentState[4] && currentState[3] != 0)) return false

  return true
}

function nextState(currentState, next){
  const newState = (currentState.state[2] == 1) ? [
        currentState.state[0] - next[0], 
        currentState.state[1] - next[1], 
        0, 
        currentState.state[3] + next[0], 
        currentState.state[4] + next[1], 
        1
      ] 
      :  [
          currentState.state[0] + next[0], 
          currentState.state[1] + next[1], 
          1, 
          currentState.state[3] - next[0], 
          currentState.state[4] - next[1], 
          0
      ]

  const inicial = currentState.distanceInicial + hammingDistance(currentState.state, newState)
  const nextNode = {
    parent: currentState,
    distanceInicial: inicial,
    totalDistance: inicial + hammingDistance(newState, final.state),
    state: newState,
    children: []
  }

  if(validState(nextNode.state)) currentState.children.push(nextNode)
  return currentState 
}

function print(finalState){
  result = `${finalState.state[0]}m ${finalState.state[1]}c ${finalState.state[2] == 1 ? ' \uD83D\uDEF6....... ' : ' .......\uD83D\uDEF6 '} ${finalState.state[3]}m ${finalState.state[4]}c \n` + (result || '')

  if(!finalState.parent) return console.log("Resultado da busca  \n\n" + result)
  
  print(finalState.parent)
}

function createNode(node){
  const t1 = nextState(node, possibleStates[0])
  const t2 = nextState(t1, possibleStates[1])
  const t3 = nextState(t2, possibleStates[2])
  const t4 = nextState(t3, possibleStates[3])
  const t5 = nextState(t4, possibleStates[4])

  const next = t5.children.reduce((a, b) => {
      if(b.totalDistance <= a.totalDistance) a = b
      return a
    })

  visitedNode.push(next.state.toString())

  if(next.state.toString() == final.state.toString()) return print(next)
 
  return createNode(next)
}

createNode(inicio)