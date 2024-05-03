class Menu {
  static selector() {
    return '#menu'
  }

  constructor() {
    this.menu = document.querySelector(Menu.selector())
    this.dropDownButtons = document.querySelectorAll('#dropdown-button')
    this.openMenuButton = document.querySelector('#open-mobile-menu-button')
    this.mobileMenu = document.querySelector('#mobile-menu')
    this.closeMenuButton = document.querySelector('#close-menu-button')
    this.mobileDropDownButtons = document.querySelectorAll(
      '#mobile-dropdown-button',
    )
    this.invisibleClass = 'hidden'
    this.bindEventListeners()
  }

  bindEventListeners() {
    this.openMenuButton.addEventListener('click', (event) => {
      this.mobileMenu.classList.toggle(this.invisibleClass)
    })

    this.closeMenuButton.addEventListener('click', (event) => {
      this.mobileMenu.classList.toggle(this.invisibleClass)
    })

    this.mobileDropDownButtons.forEach((element) => {
      element.addEventListener('click', (event) => {
        let nextElement = element.nextElementSibling
        let svg = element.querySelector('svg')
        svg.classList.toggle('rotate-180')
        element.classList.toggle('bg-brand-purple')

        nextElement.classList.toggle(this.invisibleClass)
        if (nextElement.classList.contains(this.invisibleClass)) {
          nextElement.classList.remove(
            'transition-all',
            'ease-out',
            'duration-200',
            'opacity-100',
            'translate-y-0',
          )
          nextElement.classList.add(
            'transition-all',
            'ease-in',
            'duration-150',
            'opacity-0',
            'translate-y-1',
          )
        } else {
          nextElement.classList.remove(
            'transition-all',
            'ease-in',
            'duration-150',
            'opacity-0',
            'translate-y-1',
          )
          nextElement.classList.add(
            'transition-all',
            'ease-out',
            'duration-200',
            'opacity-100',
            'translate-y-0',
          )
        }
        // click off and close menu
        document.addEventListener('click', (event) => {
          if (
            !nextElement.contains(event.target) &&
            !element.contains(event.target)
          ) {
            let svg = element.querySelector('svg')
            // rest to defaults
            svg.classList = 'h-5 w-5 flex-none mr-3'
            element.classList =
              '-mx-3 flex w-full items-center justify-between rounded-lg py-2 pl-3 text-base font-semibold leading-7 text-white hover:bg-brand-purple-mx-3 flex w-full items-center justify-between rounded-lg py-2 pl-3 text-base font-semibold leading-7 text-white hover:bg-brand-purple'
            nextElement.classList.add(this.invisibleClass)
          }
        })
      })
    })

    // Open / Close menu via menu button
    this.dropDownButtons.forEach((element) => {
      element.addEventListener('click', (event) => {
        let nextElement = element.nextElementSibling
        let svg = element.querySelector('svg')

        svg.classList.toggle('rotate-180')
        svg.classList.toggle('text-brand-purple')
        svg.classList.toggle('text-gray-400')

        nextElement.classList.toggle(this.invisibleClass)
        element.classList.toggle('text-white')
        element.classList.toggle('text-brand-purple')
        if (nextElement.classList.contains(this.invisibleClass)) {
          nextElement.classList.remove(
            'transition-all',
            'ease-out',
            'duration-200',
            'opacity-100',
            'translate-y-0',
          )
          nextElement.classList.add(
            'transition-all',
            'ease-in',
            'duration-150',
            'opacity-0',
            'translate-y-1',
          )
        } else {
          nextElement.classList.remove(
            'transition-all',
            'ease-in',
            'duration-150',
            'opacity-0',
            'translate-y-1',
          )
          nextElement.classList.add(
            'transition-all',
            'ease-out',
            'duration-200',
            'opacity-100',
            'translate-y-0',
          )
        }
        // click off and close menu
        document.addEventListener('click', (event) => {
          if (
            !nextElement.contains(event.target) &&
            !element.contains(event.target)
          ) {
            let svg = element.querySelector('svg')
            // rest to defaults
            svg.classList =
              'h-5 w-5 flex-none text-gray-400 group-hover:text-brand-purple'
            element.classList =
              'group hover:text-brand-purple flex items-center gap-x-1 text-sm font-extrabold uppercase leading-6 text-white'

            nextElement.classList.toggle(this.invisibleClass)
            nextElement.classList.add(this.invisibleClass)
          }
        })
      })
    })
  }
}

export default Menu
