var tiles = document.getElementsByClassName('game-tile')
console.log(tiles, tiles.length)
var tileArr = []

for (var i = 0; i < tiles.length; i++) {
  tileArr.push(tiles[0])
}

console.log(tileArr)

// var flashTile = style.backgroundColor = "rgba(0,0,0,0)"

// setInterval(function(){
//   var tile = tiles[Math.floor(Math.random()*tiles.length)]
//   tile.style.backgroundColor = "rgba(0,0,0,0)"
//   console.log(tile);
// }, 1000);



document.body.onkeyup = function(e){
  if(e.keyCode==32) {
    var i = Math.floor(Math.random()*tileArr.length)
    console.log(i)
    var tile = tileArr[i]
    tile.style.backgroundColor = "rgba(0,0,0,0)"
    tileArr.splice(i, 1)
    console.log(tileArr)
  }
}

// setInterval(function() {
//   // console.log("outer")
//   var tile = tiles[Math.floor(Math.random()*tiles.length)]
//   setInterval(function(){
//     tile.style.backgroundColor = "rgb(220,0,0)"
//     console.log("inner")
//   },1500)
//   tile.style.backgroundColor = "rgb(220,220,220)"
//   console.log("outer2")
// },500)

// setInterval(function(){
//   var tile = tiles[Math.floor(Math.random()*tiles.length)]
//   window.setTimeout()
// },2000)
