const path = require("path");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyPlugin = require("copy-webpack-plugin");

const options = {
        mode: "production",
    entry: "./yotta/static_src/js/main.js",
    output: {
        filename: "[name].js",
        path: path.resolve(__dirname, './yotta/static_compiled'),
        clean: true,
    },
    plugins: [new MiniCssExtractPlugin({
            filename: "[name].css",
        }),
        new CopyPlugin({
            patterns: [{
                from: "yotta/static_src/favicons/",
                to: "favicons/"
            }, {
                from: 'images',
                context: path.resolve(`./yotta/static_src/`),
                to: path.resolve(`./yotta/static_compiled/images`)
                        },
                {
                    from: 'fonts',
                    context: path.resolve(`./yotta/static_src/`),
                    to: path.resolve(`./yotta/static_compiled/fonts`)
                }],
        }),
    ],
    module: {
        rules: [{
            test: /\.css$/,
            use: [
                MiniCssExtractPlugin.loader,
                "css-loader",
                "postcss-loader"
            ]
        },
        {
            // sync font files referenced by the css to the fonts directory
            // the publicPath matches the path from the compiled css to the font file
            // only looks in the fonts folder so pngs in the images folder won't get put in the fonts folder
            test: /\.(woff|woff2)$/,
            include: /fonts/,
            type: 'asset/resource',
        },]
    },
};
    const webpackConfig = (environment, argv) => {
        const isProduction = argv.mode === 'production';
    
        options.mode = isProduction ? 'production' : 'development';
    
        if (!isProduction) {
            // https://webpack.js.org/configuration/stats/
            const stats = {
                // Tells stats whether to add the build date and the build time information.
                builtAt: false,
                // Add chunk information (setting this to `false` allows for a less verbose output)
                chunks: false,
                // Add the hash of the compilation
                hash: false,
                // `webpack --colors` equivalent
                colors: true,
                // Add information about the reasons why modules are included
                reasons: false,
                // Add webpack version information
                version: false,
                // Add built modules information
                modules: false,
                // Show performance hint when file size exceeds `performance.maxAssetSize`
                performance: false,
                // Add children information
                children: false,
                // Add asset Information.
                assets: false,
            };
    
            options.stats = stats;
    
            // Create JS source maps in the dev mode
            // See https://webpack.js.org/configuration/devtool/ for more options
            options.devtool = 'inline-source-map';
    
            // See https://webpack.js.org/configuration/dev-server/.
            options.devServer = {
                // Enable gzip compression for everything served.
                compress: true,
                static: false,
                hot: true,
                watchFiles: ['yotta/templates/', 'yotta/static_src/'],
                host: '0.0.0.0',
                // When set to 'auto' this option always allows localhost, host, and client.webSocketURL.hostname
                allowedHosts: 'auto',
                port: 3000,
                proxy: [{
                    context: () => true,
                    target: 'http://localhost:8000',
                }],
                client: {
                    // Shows a full-screen overlay in the browser when there are compiler errors.
                    overlay: true,
                    logging: 'error',
                },
                devMiddleware: {
                    index: true,
                    publicPath: '/static/',
                    writeToDisk: true,
                    stats,
                },
            };
        }
    
        return options;
    };
    
    module.exports = webpackConfig;