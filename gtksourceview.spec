Summary:	Text widget that extends the standard GTK+ 2.x
Summary(pl):	Widget tekstowy rozszerzaj±cy standardowy z GTK+ 2.x
Name:		gtksourceview
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	e9c04b40f1f44dd6ab6a95f7ad7b7258
URL:		http://www.gnome.org/
BuildRequires:	gnome-vfs2-devel >= 2.3.7
BuildRequires:	gtk+2-devel >= 2.2.2
BuildRequires:	libgnomeprintui-devel >= 2.3.1
BuildRequires:	libxml2-devel >= 2.5.10
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
Requires:	%{name} = %{version}
Requires:	gtk-doc-common
Requires:	gtk+2-devel >= 2.2.2
Requires:	libgnomeprint-devel >= 2.3.1
Requires:	libxml2-devel >= 2.5.10

%description devel
Header files for gtktextview.

%description devel -l pl
Pliki nag³ówkowe dla gtktextview.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}

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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/*
%{_gtkdocdir}/%{name}
