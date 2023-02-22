chat = []

function newmsg(dat){
  chat.unshift(dat)
  if (chat.length > 4){chat.shift()}
}
