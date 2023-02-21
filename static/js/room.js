
	window.scramble = ""
	
  window.user_name = prompt("Hello. Please enter your name")
		async function send(name,time) {
			var socket = io();
			var ca = time.value
			if (ca != '') 
			{socket.on('connect', function() {
        var x = socket.emit('update', {data: `{"time":"${ca}","name":"${name}","id":${window.id}}`});
				
				
    });
		}
		time.value = '';
		}
	
	function upd(nm){
		var ele = document.getElementById("out")
		ele.innerHTML = ""
		for (const k in nm){

			ele.innerHTML += `${k} : ${nm[k]}<br>`
		}
	}
	var socket = io();
	var ul =new  URLSearchParams(location.search)
	if (ul.get("ID") == "" || ul.get("ID") == null){
		window.focus()
    if (ul.get("new") != "" && ul.get("new") != null){
      uip = "N"
    }
    else{
		var uip = prompt("N for new room, or J to join an exsisting room")
    }
		if (uip == "N"){
			window.id = Math.round(Math.random()*100000)
			socket.emit("getIDR",{"data":window.id})
      if (ul.get("event") == "" || ul.get("event")  ==null)
      {
        window.event = prompt("Event: ")
      }
      else{
        window.event = ul.get("event")
      }
			socket.emit('setEVN',{id:window.id,evn:window.event})
			document.getElementById("footer").innerHTML = (`room ID: ${window.id}`)
			
		}
		else if (uip == "J"){
			window.id = prompt("Please enter the room ID")
			
			document.getElementById("footer").innerHTML = (`room ID: ${window.id}`)
		}
	}
	else{
		
	 window.id =ul.get("ID")
		
	}

	document.getElementById("gl").addEventListener("click",(e)=>{
    navigator.clipboard.writeText(`${window.location.href.split('?')[0]}?ID=${window.id}`);
    alert("link copied")

  })
	socket.on("retupdate",function(msg) {
		inid = msg[1]
		console.log(msg)
		var js = JSON.parse(msg[0]);
		if (inid == window.id){upd(js)}
	})
	socket.on("newscramb",function(s) {
		if (s[1] == window.id){
			window.scramble = s[0];
			document.getElementById("sc").innerHTML = s[0];
		}
	})
	
	
	function cl(){
		var socket = io();
		socket.on('connect', function() {
        var x = socket.emit('newr', {data: window.id});
				
    });

	}
	function chevn() {
    var ev = ["3x3","2x2","4x4","5x5","pyraminx","skewb","clock","3bld"]
		window.event = prompt("Event: ")
    if (ev.includes(window.event)){
		socket.emit('setEVN',{id:window.id,evn:window.event})
    }
    else{
      alert(`${window.event} is not a valid event`)
    }
	}
