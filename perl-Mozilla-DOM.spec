#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mozilla
%define		pnam	DOM
Summary:	Mozilla::DOM - Mozilla DOM interface wrapper for Perl
Summary(pl.UTF-8):	Mozilla::DOM - perlowy wrapper interfejsu Mozilla DOM
Name:		perl-Mozilla-DOM
Version:	0.20
Release:	1
# note if it is "same as perl"
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mozilla/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e2b3cc11dba8b327f8df03908ceed3d4
Patch0:		%{name}-xulrunner.patch
Patch1:		%{name}-man.patch
URL:		http://search.cpan.org/dist/Mozilla-DOM/
BuildRequires:	libstdc++-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	xulrunner-devel >= 1.8
%requires_eq	xulrunner-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	libxpcom.so

%description
This module wraps the Mozilla DOM interface in Perl.

In conjuction with an embedded Gecko widget (e.g. Gtk2::MozEmbed),
you can use Perl to manipulate the browser DOM, handle DOM signals,
and create events such as mouse clicks -- all within a Mozilla-like
browser (so it also does JavaScript). See `perldoc Mozilla::DOM`
for more details.

%description -l pl.UTF-8
Ten moduł obudowuje interfejs Mozilla DOM w Perlu.

W połączeniu z osadzonym widgetem Gecko (np. Gtk2::MozEmbed) pozwala
używać Perla do manipulacji DOM przeglądarki, obsługi sygnałów DOM,
tworzenia zdarzeń takich jak kliknięcia myszką - wszystko wewnątrz
mozillowatej przeglądarki (więc także obsługuje JavaScript). Więcej
szczegółów w `perldoc Mozilla::DOM`.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Mozilla/DOM/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Credits README TODO
# XXX: shared with perl-Mozilla-LDAP
%dir %{perl_vendorarch}/Mozilla
%{perl_vendorarch}/Mozilla/DOM.pm
%dir %{perl_vendorarch}/Mozilla/DOM
%{perl_vendorarch}/Mozilla/DOM/*.pm
%{perl_vendorarch}/Mozilla/DOM/Install
# XXX: shared with perl-Mozilla-LDAP
%dir %{perl_vendorarch}/auto/Mozilla
%dir %{perl_vendorarch}/auto/Mozilla/DOM
%{perl_vendorarch}/auto/Mozilla/DOM/DOM.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Mozilla/DOM/DOM.so
%{_mandir}/man3/Mozilla::DOM*.3pm*
