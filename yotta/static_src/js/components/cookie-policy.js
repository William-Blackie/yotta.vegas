class CookiePolicy {
  static selector() {
    return '#cookie-policy'
  }

  constructor() {
    this.cookiePolicy = document.querySelector(CookiePolicy.selector())
    this.cookiePolicyButton = document.querySelector('#dismiss-cookie-policy')
    this.invisibleClass = 'hidden'
    if (document.cookie.includes('cookie_policy=accepted')) {
      this.cookiePolicy.classList.toggle(this.invisibleClass)
    }
    this.bindEventListeners()
  }

  bindEventListeners() {
    this.cookiePolicyButton.addEventListener('click', (event) => {
      this.cookiePolicy.classList.toggle(this.invisibleClass)
      // set cookie
      document.cookie =
        'cookie_policy=accepted; expires=Fri, 31 Dec 9999 23:59:59 GMT'
    })
  }
}

export default CookiePolicy
