var gulp = require('gulp');
// var sass = require('gulp-ruby-sass');
var autoprefixer = require('gulp-autoprefixer');
var minifycss = require('gulp-minify-css');
var less = require('gulp-less');
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var rename = require('gulp-rename');
var debug = require('gulp-debug');
var fs = require('fs');

// var clean = require('gulp-clean');
var concat = require('gulp-concat');
var notify = require('gulp-notify');
var cache = require('gulp-cache');

// pour less/css
var d = "./src/rmi/site/skins/rmi.site/"

var lessfiles = [d + 'rmi-site.less'];
w = process.cwd();
styles = gulp.task(
    'styles',
    function() {
        return gulp.src(lessfiles)
        .pipe(less())
        .pipe(autoprefixer('last 2 versions', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
        //.pipe(autoprefixer({
        // 	browsers: ['last 2 version', 'safari 5', 'ie6', 'ie7', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4']
        // }))
        .pipe(rename("rmi-site.css"))
        .pipe(gulp.dest(d))
        .pipe(notify({message: 'Styles task complete'}))
        .pipe(minifycss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(d))
        .pipe(notify({message: 'Styles task min complete'}));
    });
gulp.task('default', ['styles']);
gulp.task('watch', function() {
  gulp.watch(lessfiles, ['styles']);
  /* gulp.watch(javascripts, ['js']); */
});

// fin pour less/css

// pour doc
var docsfiles = ['docs/*.rst'];
var readme = 'README.rst'
var shell = require('gulp-shell')
gulp.task('build-docs', shell.task('bin/sphinx-build docs docs/html', {cwd: '.'}))
gulp.task('readme', shell.task('cp README.rst docs', {cwd: '.'}))
gulp.task('docs', ['build-docs'], function() {
  gulp.watch(readme, ['readme'])
  gulp.watch(['./docs/*.rst', './docs/*.py'], ['build-docs'])
})
// fin pour doc


/*
js = gulp.task(
    'js',
    function() {
        return gulp.src(javascripts)
        .pipe(concat('script.js'))
        .pipe(gulp.dest(d+'js/'))
        .pipe(uglify())
        .pipe(rename('script.min.js'))
        .pipe(gulp.dest(d+'js/'))
        .pipe(notify({message: 'JS task complete'}));
    });
fonts = gulp.task(
    'fonts',
    function() {
        return gulp.src([
            './bower_components/font-awesome/fonts/**',
        ])
        .pipe(gulp.dest(d+'fonts/'))
        .pipe(notify({message: 'FONTS task complete'}));
    });
*/
/* vim:set ft=javascript : */
