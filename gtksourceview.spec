#
# Conditional build:
%bcond_without	gnome	# disable gnomeprint support, don't build tests
#
Summary:	Text widget that extends the standard GTK+ 2.x
Summary(pl.UTF-8):	Widget tekstowy rozszerzający standardowy z GTK+ 2.x
Name:		gtksourceview
Version:	1.8.5
Release:	8
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtksourceview/1.8/%{name}-%{version}.tar.bz2
# Source0-md5:	de67df2944c1cccbc2d0b4a738e11050
Patch0:		%{name}-nognome.patch
Patch1:		%{name}-build-fix.patch
Patch2:		format-security.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	gnome-common >= 2.12.0
%{?with_gnome:BuildRequires:	gnome-vfs2-devel >= 2.17.91}
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.35.5
%{?with_gnome:BuildRequires:	libgnomeprintui-devel >= 2.17.92}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceView is a text widget that extends the standard GTK+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

%description -l pl.UTF-8
GtkSourceView to widget tekstowy rozszerzający standardowy widget
tekstowy GtkTextView z GTK+ 2.x. Ulepsza GtkTextView poprzez
zaimplementowanie podświetlania składni i innych możliwości typowych
dla edytora źródeł.

%package apidocs
Summary:	GtkSourceView API documentation
Summary(pl.UTF-8):	Dokumentacja API GtkSourceView
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GtkSourceView API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GtkSourceView.

%package devel
Summary:	Header files for gtktextview
Summary(pl.UTF-8):	Pliki nagłówkowe dla gtktextview
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.9
%{?with_gnome:Requires:	libgnomeprint-devel >= 2.17.92}
Requires:	libxml2-devel >= 1:2.6.27

%description devel
Header files for gtktextview.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gtktextview.

%package static
Summary:	Static gtksourceview library
Summary(pl.UTF-8):	Statyczna biblioteka gtksourceview
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtksourceview library.

%description static -l pl.UTF-8
Statyczna biblioteka gtksourceview.

%prep
%setup -q
%{!?with_gnome:%patch0 -p1}
%patch1 -p1
%patch2 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gnome:--disable-gnomeprint} \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}-1.0

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtksourceview-1.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtksourceview-1.0.so.0
%{_datadir}/%{name}-1.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-1.0.so
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/gtksourceview-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceview-1.0.a
