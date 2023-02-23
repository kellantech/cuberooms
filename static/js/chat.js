chat = []

function newmsg(dat){
  chat.push(dat)
  if (chat.length > 4){chat.shift()}
}
