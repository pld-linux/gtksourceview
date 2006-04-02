Summary:	Text widget that extends the standard GTK+ 2.x
Summary(pl):	Widget tekstowy rozszerzaj±cy standardowy z GTK+ 2.x
Name:		gtksourceview
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtksourceview/1.6/%{name}-%{version}.tar.bz2
# Source0-md5:	f3403c0f8c5f924b022534b0d93d8e0f
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.31
BuildRequires:	libgnomeprintui-devel >= 2.11.0-3
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.21
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

%package devel
Summary:	Header files for gtktextview
Summary(pl):	Pliki nag³ówkowe dla gtktextview
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-doc-common
Requires:	gtk+2-devel >= 2:2.8.3
Requires:	libgnomeprintui-devel >= 2.11.0-3
Requires:	libxml2-devel >= 1:2.6.21

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}-1.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/*
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
