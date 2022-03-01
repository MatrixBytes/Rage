const mineflayer = require('mineflayer');

try {
    const bot = mineflayer.createBot({
        host: process.argv[2],
        username: '', // account email or username
        password: '', // account password
        auth: '', // account type (mojang or microsoft)
        version: '1.18.1', // version u wanna scan (1.18.1 recommendet)
        hideErrors: "True"
    });

    bot.once('spawn', () => {
        console.log('false')
        bot.quit()
    });

    bot.once('kicked', () => {
        console.log('true')
    })

    bot.once('error', () => {
        console.log('true')
    })
} 

catch {
    console.log('true')
}