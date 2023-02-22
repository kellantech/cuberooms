chat = []

function newmsg(dat){
  chat.unshift(dat)
  if (chat.length > 10){chat.shift()}
}
