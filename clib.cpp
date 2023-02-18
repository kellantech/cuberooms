// cppimport
 


#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <string>
	
namespace py = pybind11;
#include <iostream>
#include <map>
#include <time.h>
using namespace std;



class room{
	public:
	map<string,string> cur;
	string scramb;
	string event;
	room(){}
	void set(string name, string time){
		cur[name] = time;
	}
	string get(string name){
		return cur[name];
	}
	map<string,string> getall(){
		return cur;
	}


};



map<int,room>rids;

int newr(){
	srand(time(NULL));

	int id = rand();
	room emptr = room();
	rids[id] = emptr;
	return id;
}
void clear(int rid){
	rids[rid].cur = {};
}

map<string,string> getr(int rid){
	return rids[rid].getall();
}

void setrom(int rid,string name, string time){
	rids[rid].set(name,time);
}

void _MSF_(void){}

void parse(map<string,string> m){
	int id = stoi(m["id"]);
	string name = m["name"];
	string time = m["time"];
	setrom(id,name,time);
}



string get_scramb(int id){
	return rids[id].scramb;
}
void set_scramb(int id,string sc){
	rids[id].scramb = sc;
}

void set_event(int id,string ev){
	rids[id].event = ev;
}

string get_event(int id){
	return rids[id].event;
}



PYBIND11_MODULE(clib, m) {
    
		m.def("_MSF_", &_MSF_);
		m.def("new",&newr);
		m.def("get",&getr);
		m.def("setrom",&setrom);
		m.def("parse",&parse);
		m.def("clear",&clear);
		m.def("set_event",&set_event);
		m.def("get_event",&get_event);
}


/*
<%
setup_pybind11(cfg)
%>
*/
