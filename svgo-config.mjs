// import { extendDefaultPlugins } from 'svgo'

export default {
  plugins: [
    {
      name: 'removeUnknownsAndDefaults',
      active: false
    },
    {
      name: 'removeUselessDefs',
      active: false
    },
    {
      name: 'removeUselessStrokeAndFill',
      active: false
    }
  ]
}