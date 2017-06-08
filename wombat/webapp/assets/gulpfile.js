'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', function () {
 return gulp.src('./sass/main.scss')
   .pipe(sass().on('error', sass.logError))
   .pipe(gulp.dest('../static/css'));
});

gulp.task('default', function() {
	gulp.watch('./sass/**/*.scss', ['sass']);
});
