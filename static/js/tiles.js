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




// const delay = ms => new Promise(res=>setTimeout(res, ms))
// const flashTile = async() => {
//   await delay(1000)
//   console.log("waited 1s")
//   await delay(1000)
//   console.log("wait additional 1s")
// }



// var flashTile = style.backgroundColor = "rgba(0,0,0,0)"

// setInterval(function(){
//   var tile = tiles[Math.floor(Math.random()*tiles.length)]
//   tile.style.backgroundColor = "rgba(0,0,0,0)"
//   console.log(tile);
// }, 1000);

// function removeTile(arr) {
//
// }


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
