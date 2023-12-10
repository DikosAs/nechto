// константы и общая информация
//////////////////////////////////////////////////////////////////////////////////////
const BASE_URL = document.URL.replace('game.html', '')
const CSRF = document.getElementsByName('csrfmiddlewaretoken')[0].value

async function load_base_data() {
    await fetch(`${BASE_URL}get-all-cards-data`)
      .then(res => {
          if (res.ok){
              return res.json()
          } else {
              console.log("ERROR: Карты не загруженны")
              return {}
          }
        })
      .then(data => {
        CARDS_DATA = data['cards']
        return CARDS_DATA
      })
}

let CARDS_DATA = load_base_data()

// Запрос к подключению
//////////////////////////////////////////////////////////////////////////////////////
fetch(
    `${BASE_URL}add-player-id-game`,
    {
        method: "POST",
        headers: {
            'X-CSRFToken': CSRF
        }
    }
)
    
// Добаление кнопки выёти из игры
//////////////////////////////////////////////////////////////////////////////////////
document.querySelector('div.nav-link#play a').setAttribute('href', 'exit')
document.querySelector('div.nav-link#play a').textContent = 'Выход из игры'
document.querySelector('div.nav-link#play').setAttribute('style', 'width: 150px;')

let users_html = document.querySelector('div.players')
let user_cards = document.querySelector('div.my-cards')

async function update() {
    // Обновление списка игроков
    let users_data, users_lenth
    {await fetch(`${BASE_URL}get-users-data`)
      .then(res => {
        if (res.ok){
            return res.json()
        } else {
            console.log("ERROR: Игроки не загруженны")
            return {'users': [], 'users_lenth': 0}
        }
      })
      .then(data => {
        users_data = data['users']
        users_lenth = data['users_lenth']
      })
    
    for (let userID = 1; userID <= users_lenth; userID++) {
        users_html.innerHTML = `
        <div class="payer">
        <div class="player-name">${users_data[userID].name}</div>
        </div>
        `
    }}
    
    // Обновление карт у игрока
    let cards
    await fetch(`${BASE_URL}get-user-cards`)
}   
    
// Запуск обновлений
setTimeout(() => {
    update()
    setInterval(() => {update()}, 10000)
    console.log(CARDS_DATA)
}, 250)