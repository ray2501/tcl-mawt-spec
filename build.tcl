#!/usr/bin/tclsh

set arch "x86_64"
set base "mawt-0.4.0"
set fileurl "http://www.mawt.tcl3d.org/download/mawt-0.4.0.zip"

set var [list wget $fileurl -O $base.zip]
exec >@stdout 2>@stderr {*}$var

set useArchive 1
if {[catch {package require archive} errMsg] == 1} {
    puts $errMsg
    set useArchive 0
}

if {$useArchive==1} {
    archive::extract $base.zip all all 1
    archive::create $base.tar.gz gzip ustar [list $base]
} else {
    set var2 [list unzip $base.zip]
    exec >@stdout 2>@stderr {*}$var2

    set var2 [list tar czvf $base.tar.gz $base]
    exec >@stdout 2>@stderr {*}$var2
}

file delete -force $base.zip
file delete -force $base

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force CMakeLists.patch build/SOURCES
file copy -force CMakeModules.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl-mawt.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove source package
file delete -force $base.tar.gz
