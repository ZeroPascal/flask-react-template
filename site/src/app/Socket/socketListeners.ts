import { Dispatch } from "react";
import { Socket } from "socket.io-client";

export default function socketListeners(socket: Socket, d: Dispatch<any>){
    socket.onAny((event,payload)=>{
        console.log(socket.id)
        console.log(event,payload)
        switch(event){
      
         
        }
    })

}
