function ConsoleMessage() {
  const console_style =
    'color: #fff; background: #000; padding: 5px 10px; border-radius: 5px;'
  console.log('%cHi there! 👋', console_style)
  console.log(
    '%cSend me a message to say hello: will@developerfy.com',
    console_style,
  )
}

export default ConsoleMessage
