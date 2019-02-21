var names = [1,2,3,4,5]

const pick = document.getElementById('pick-player')
pick.addEventListener('click', ()=>{
  name = names[Math.floor(Math.random()*names.length)]
  document.getElementById('player-name').innerHTML = name
  console.log(name)
})
