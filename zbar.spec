Name:           zbar
Version:        0.20.1
Release:        4
Summary:        Bar code reader
License:        LGPLv2+
URL:            http://zbar.sourceforge.net/
Source0:        https://linuxtv.org/downloads/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf automake libtool gettext-devel qt5-qtbase-devel qt5-qtx11extras-devel gtk2-devel
BuildRequires:  GraphicsMagick-c++-devel libv4l-devel libXv-devel xmlto python2-devel pygtk2-devel
Requires:       pygtk2 python2-pillow
Provides:       %{name}-gtk = %{version}-%{release} %{name}-pygtk = %{version}-%{release} %{name}-qt = %{version}-%{release}
Obsoletes:      %{name}-gtk < %{version}-%{release} %{name}-pygtk < %{version}-%{release} %{name}-qt < %{version}-%{release}

%description
ZBar is an open source software suite for reading bar codes from various sources, such as video streams,
image files and raw intensity sensors. It supports many popular symbologies (types of bar codes) including
EAN-13/UPC-A, UPC-E, EAN-8, Code 128, Code 39, Interleaved 2 of 5 and QR Code.

The flexible, layered implementation facilitates bar code scanning and decoding for any application: use it
stand-alone with the included GUI and command line programs, easily integrate a bar code scanning widget into
your Qt, GTK+ or PyGTK GUI application, leverage one of the script or programming interfaces (Python, Perl,
C++) ...all the way down to a streamlined C library suitable for embedded use.

%package devel
Summary:        Bar code library extra development files
Requires:       pkgconfig %{name} = %{version}-%{release}
Provides:       %{name}-gtk-devel = %{version}-%{release} %{name}-qt-devel = %{version}-%{release}
Obsoletes:      %{name}-gtk-devel < %{version}-%{release} %{name}-qt-devel < %{version}-%{release}

%description devel
This zbar-devel package contains header files and additional libraries used for developing applications
that read bar codes with this library.

%package help
Summary:        Help package for zbar

%description help
This package contains some man help files for zbar.

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -vfi
%configure --without-java --with-graphicsmagick --docdir=%{_docdir}/%{name}-%{version}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install INSTALL="install -p"
%delete_la_and_a
rm -rf $RPM_BUILD_ROOT/usr/share/doc/zbar-%{version}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%files
%doc COPYING LICENSE NEWS
%{_bindir}/*
%{_libdir}/*.so.*
%{python2_sitearch}/*.so

%files devel
%doc HACKING TODO
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files help
%{_mandir}/man1/*

%changelog
* Tue Dec  3 2019 lingsheng <lingsheng@huawei.com> - 0.20.1-4
- Package init
