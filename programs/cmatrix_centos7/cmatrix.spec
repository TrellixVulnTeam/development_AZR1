%define name    cmatrix
%define ver     2.0
%define rel     2

Summary: CMatrix simulates the display from "The Matrix"
Name: %{name}
Version: %{ver}
Release: %{rel}
Group: Amusements/Graphics
Copyright: GPL
Packager: abishekvashok@gmail.com
URL: https://github.com/abishekvashok/cmatrix
Source0: https://github.com/abishekvashok/cmatrix/archive/%{ver}.tar.gz
Provides: none
Requires: ncurses
Conflicts: none
BuildRoot: /var/tmp/%{name}-buildroot
%Description
CMatrix is based on the screensaver from The Matrix website. It can scroll
lines all at the same rate or asynchronously and at a user-defined speed.
%Prep
%setup
%Build
./configure --prefix=/usr --mandir=/usr/share/man
make
%Install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install
mkdir -p $RPM_BUILD_ROOT/usr/lib/kbd/consolefonts
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc
strip cmatrix
install matrix.fnt $RPM_BUILD_ROOT/usr/lib/kbd/consolefonts
install matrix.psf.gz $RPM_BUILD_ROOT/usr/lib/kbd/consolefonts
install mtx.pcf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc
mkfontdir $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc
%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(-,root,root)
%doc COPYING INSTALL README.md
%{_bindir}/cmatrix
%{_mandir}/*/*
/usr/lib/kbd/consolefonts/matrix.psf.gz
/usr/lib/kbd/consolefonts/matrix.fnt
/usr/X11R6/lib/X11/fonts/misc/mtx.pcf
