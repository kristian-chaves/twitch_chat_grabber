const oAuth = "dy71ezmwmejfoyhx8pkntuya1yno2h";
//const oAuth = "5pm2jgry9oqeghu1nunqe5pprrq3iz";

const nick = "squaresyyy";
const channel = "squaresyyy";
const fs = require('fs')


Object.assign(global, { WebSocket: require('ws') });
const socket = new WebSocket('wss://irc-ws.chat.twitch.tv:443');

socket.addEventListener('open', (event) => {
    socket.send(`Pass oauth:${oAuth}`);
    socket.send(`NICK ${nick}`)
    socket.send(`JOIN #${channel}`)
})  

socket.addEventListener('message', event => {
    //save just message data
    if (event.data.includes("PRIVMSG")){
        fs.appendFile('Output.txt', event.data, (err) => {          
            // In case of a error throw err.
            if (err) throw err;
        })
            //console.log(event.data);
    }
    if(event.data.includes("PING")) socket.send("PONG");
})

