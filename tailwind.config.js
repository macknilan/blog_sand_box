/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './apps/templates/**/*.{html, js}',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
      extend: {
          fontFamily: {
              'body': ['Roboto Mono', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui'],
              'sans': ['Roboto Mono', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui'],
              'serif': ['Roboto Mono', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui'],
              'mono': ['Roboto Mono', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui']
          },
      colors: {
        'primary': 'oklch(65.69% 0.196 275.75)',
        'secondary': 'oklch(74.8% 0.26 342.55)',
        'accent': 'oklch(74.51% 0.167 183.61)',
        'neutral': '#2a323c',
        'neutral-content': '#A6ADBB',
        'base-100': '#1d232a',  // BACKGROUND 2
        'base-200': '#191e24',
        'base-300': '#15191e',
        'base-content-1': '#A6ADBB',
        'base-content': {
            '50': '#f5f6f6',
            '100': '#e5e7e8',
            '200': '#cdd1d4',
            '300': '#aab2b6',
            '400': '#808b90',
            '500': '#657075',
            '600': '#565e64',
            '700': '#4a5054',
            '800': '#414549',
            '900': '#393c40',
            '950': '#1d1f21',  // 👈 BACKGROUND 1
        },
        'silver': {
            '50': '#f6f6f7',
            '100': '#efeff0',
            '200': '#e2e2e3',
            '300': '#c9cacc',  // 👈
            '400': '#bbbbbe',
            '500': '#a8a9ac',
            '600': '#939498',
            '700': '#7f8083',
            '800': '#68686b',
            '900': '#565659',
            '950': '#323234',
        },
        'mint': {
            '50': '#eefbf5',
            '100': '#d6f5e5',
            '200': '#b1e9ce',
            '300': '#7dd8b3',
            '400': '#48bf92',
            '500': '#2bbc8a',  // 👈
            '600': '#178461',
            '700': '#136950',
            '800': '#115440',
            '900': '#0f4536',
            '950': '#07271f',
        },
        'anti-flash-white': {
            '50': '#ffffff',
            '100': '#fcfcfc',
            '200': '#fafafa',
            '300': '#f7f7f7',
            '400': '#f2f2f2',
            '500': '#eeeeee',  // 👈
            '600': '#d6c1c1',
            '700': '#b38686',
            '800': '#8f5656',
            '900': '#6b3030',
            '950': '#451414'
        },
        'dim-gray': {
            '50': '#f7f7f7',
            '100': '#f0f0f0',
            '200': '#d9d9d9',
            '300': '#c2c2c2',
            '400': '#949494',
            '500': '#666666',  // 👈
            '600': '#5c5353',
            '700': '#4d3939',
            '800': '#3d2525',
            '900': '#2e1515',
            '950': '#1f0909'
        },
      },
     },
  },
  plugins: [
      require('flowbite/plugin')
  ]
}

