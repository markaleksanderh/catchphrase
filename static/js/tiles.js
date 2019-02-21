var tiles = document.getElementsByClassName('game-tile')
var tileArr = []

for (var i = 0; i < tiles.length; i++) {
  tileArr.push(tiles[i])
}

document.body.onkeyup = function(e){
  if(e.keyCode==32) {
    let i = Math.floor(Math.random()*tileArr.length)
    let tile = tileArr[i]
    tile.style.background = "None"
    tile.style.backgroundColor = "rgba(0,0,0,0)"
    tileArr.splice(i, 1)
  }
}
