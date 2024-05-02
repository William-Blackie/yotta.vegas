/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
    content: [
        './yotta/templates/**/*.{html,js}',
        './yotta/utils/constants.py',
    ],
    darkMode: 'selector',
    theme: {
        fontSize: {
            xs: ['0.75rem', { lineHeight: '1rem' }],
            sm: ['0.875rem', { lineHeight: '1.5rem' }],
            base: ['1rem', { lineHeight: '1.75rem' }],
            lg: ['1.125rem', { lineHeight: '1.75rem' }],
            xl: ['1.25rem', { lineHeight: '2rem' }],
            '2xl': ['1.5rem', { lineHeight: '2.25rem' }],
            '3xl': ['1.75rem', { lineHeight: '2.25rem' }],
            '4xl': ['2rem', { lineHeight: '2.5rem' }],
            '5xl': ['2.5rem', { lineHeight: '3rem' }],
            '6xl': ['3rem', { lineHeight: '3.5rem' }],
            '7xl': ['4rem', { lineHeight: '4.5rem' }],
        },
        extend: {
            borderRadius: {
                '4xl': '2.5rem',
            },
            fontFamily: {
                sans: ['MolendRegular', ...defaultTheme.fontFamily.sans],
                display: [
                    ['Molend', ...defaultTheme.fontFamily.sans],
                    { fontVariationSettings: '"wdth" 125' },
                ],
            },
            colors: {
                "brand-purple": "#7231FF",
                "brand-green": "#66FF58",
            },
            animation: {
                "marquee": "marquee 250s linear infinite",
            },  
        },
    },
    plugins: [],
}
