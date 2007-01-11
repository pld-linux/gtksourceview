Summary:	Text widget that extends the standard GTK+ 2.x
Summary(pl):	Widget tekstowy rozszerzaj±cy standardowy z GTK+ 2.x
Name:		gtksourceview
Version:	1.8.3
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtksourceview/1.8/%{name}-%{version}.tar.bz2
# Source0-md5:	1da36ae813b6234dc9d327c3500afef9
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-vfs2-devel >= 2.16.3
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnomeprintui-devel >= 2.12.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceView is a text widget that extends the standard GTK+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

%description -l pl
GtkSourceView to widget tekstowy rozszerzaj±cy standardowy widget
tekstowy GtkTextView z GTK+ 2.x. Ulepsza GtkTextView poprzez
zaimplementowanie pod¶wietlania sk³adni i innych mo¿liwo¶ci typowych
dla edytora ¼róde³.

%package apidocs
Summary:	GtkSourceView API documentation
Summary(pl):	Dokumentacja API GtkSourceView
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GtkSourceView API documentation.

%description apidocs -l pl
Dokumentacja API GtkSourceView.

%package devel
Summary:	Header files for gtktextview
Summary(pl):	Pliki nag³ówkowe dla gtktextview
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.7
Requires:	libgnomeprintui-devel >= 2.12.1
Requires:	libxml2-devel >= 1:2.6.27

%description devel
Header files for gtktextview.

%description devel -l pl
Pliki nag³ówkowe dla gtktextview.

%package static
Summary:	Static gtksourceview library
Summary(pl):	Statyczna biblioteka gtksourceview
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtksourceview library.

%description static -l pl
Statyczna biblioteka gtksourceview.

%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-static \
	--enable-gtk-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}-1.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
