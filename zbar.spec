Name:		zbar
Version:	0.22
Release:	1
Summary:	Bar code reader
License:	LGPLv2+
URL:		http://zbar.sourceforge.net/
Source0:	https://linuxtv.org/downloads/zbar/zbar-%{version}.tar.bz2

BuildRequires:       	autoconf automake libtool gettext-devel
BuildRequires:       	qt5-qtbase-devel qt5-qtx11extras-devel 	gtk2-devel GraphicsMagick-c++-devel
BuildRequires:       	libv4l-devel libXv-devel xmlto dbus-devel

%description
A layered bar code scanning and decoding library. Supports EAN, UPC, Code 128,
Code 39 and Interleaved 2 of 5.
Includes applications for decoding captured bar code images and using a video
device (e. g., webcam) as a bar code scanner.

%package devel
Summary:             Bar code library extra development files
Requires:            pkgconfig, zbar = %{version}-%{release}

%description devel
This package contains header files and additional libraries used for
developing applications that read bar codes with this library.

%package gtk
Summary:             Bar code reader GTK widget
Requires:            zbar = %{version}-%{release}

%description gtk
This package contains a bar code scanning widget for use with GUI
applications based on GTK+-2.0.

%package gtk-devel
Summary:             Bar code reader GTK widget extra development files
Requires:            pkgconfig, zbar-gtk = %{version}-%{release}, zbar-devel = %{version}-%{release}

%description gtk-devel
This package contains header files and additional libraries used for
developing GUI applications based on GTK+-2.0 that include a bar code
scanning widget.

%package qt
Summary:             Bar code reader Qt widget
Requires:            zbar = %{version}-%{release}

%description qt
This package contains a bar code scanning widget for use with GUI
applications based on Qt4.

%package qt-devel
Summary:             Bar code reader Qt widget extra development files
Requires:            pkgconfig, zbar-qt = %{version}-%{release}, zbar-devel = %{version}-%{release}

%description qt-devel
This package contains header files and additional libraries used for
developing GUI applications based on Qt4 that include a bar code
scanning widget.

%prep
%setup -q

%build
autoreconf -vfi
%configure --without-java --with-graphicsmagick --without-python2 --docdir=%{_docdir}/zbar-%{version}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find ${RPM_BUILD_ROOT} -name '*.la' -or -name '*.a' | xargs rm -f
rm -rf $RPM_BUILD_ROOT/usr/share/doc/zbar-%{version}/
%ldconfig_scriptlets
%ldconfig_scriptlets devel
%ldconfig_scriptlets gtk
%ldconfig_scriptlets qt

%files
%doc NEWS README.md INSTALL.md
%license COPYING LICENSE
%{_bindir}/zbarimg
%{_bindir}/zbarcam
%{_libdir}/libzbar.so.*
%{_mandir}/man1/*
%{_sysconfdir}/dbus-1/system.d/org.linuxtv.Zbar.conf

%files devel
%doc HACKING TODO
%{_libdir}/libzbar.so
%{_libdir}/pkgconfig/zbar.pc
%dir %{_includedir}/zbar
%{_includedir}/zbar.h
%{_includedir}/zbar/Exception.h
%{_includedir}/zbar/Symbol.h
%{_includedir}/zbar/Image.h
%{_includedir}/zbar/Scanner.h
%{_includedir}/zbar/Decoder.h
%{_includedir}/zbar/ImageScanner.h
%{_includedir}/zbar/Video.h
%{_includedir}/zbar/Window.h
%{_includedir}/zbar/Processor.h

%files gtk
%{_libdir}/libzbargtk.so.*
%{_bindir}/zbarcam-gtk

%files gtk-devel
%{_libdir}/libzbargtk.so
%{_libdir}/pkgconfig/zbar-gtk.pc
%{_includedir}/zbar/zbargtk.h

%files qt
%{_libdir}/libzbarqt.so.*
%{_bindir}/zbarcam-qt

%files qt-devel
%{_libdir}/libzbarqt.so
%{_libdir}/pkgconfig/zbar-qt.pc
%{_includedir}/zbar/QZBar*.h

%changelog
* Thu Oct 22 2020 caodongxia <caodongxia@huawei.com> - 0.22-1
- update package from 0.20.1 to 0.22

* Tue Dec 3 2019 lingsheng <lingsheng@huawei.com> - 0.20.1-4
- Package init
