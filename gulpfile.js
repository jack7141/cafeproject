//해당 파일은 그냥 가져다 써도 무방함

const gulp = require("gulp");

const css = () => {
  const postCSS = require("gulp-postcss");
  var sass = require('gulp-sass')(require('sass'));
  const minify = require("gulp-csso");
  sass.compiler = require("node-sass");
  return gulp
//    gulp파일을 저장할 경로 설정
    .src("assets/scss/styles.scss")
    .pipe(sass().on("error", sass.logError))
    .pipe(postCSS([require("tailwindcss"), require("autoprefixer")]))
    .pipe(minify())
//    처리후 최종 저장할 곳 위치 설정
    .pipe(gulp.dest("static/css"));
};

exports.default = css;