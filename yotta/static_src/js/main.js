import '../css/main.css'
import ConsoleMessage from './components/console-message'
import Menu from './components/menu'
import CookiePolicy from './components/cookie-policy'

document.addEventListener('DOMContentLoaded', () => {
  if (document.querySelector(Menu.selector())) {
    new Menu()
  }
  if (document.querySelector(CookiePolicy.selector())) {
    new CookiePolicy()
  }


  ConsoleMessage()
})
