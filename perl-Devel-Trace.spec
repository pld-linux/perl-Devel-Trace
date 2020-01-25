#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%define		pdir	Devel
%define		pnam	Trace
Summary:	Devel::Trace - print out each line before it is executed (like `sh -x')
Summary(pl.UTF-8):	Devel::Trace - wypisywanie każdej linii przed wykonaniem (jak `sh -x')
Name:		perl-Devel-Trace
Version:	0.11
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1138fe5d16b446dca3d55ccea37d8b96
URL:		http://www.plover.com/~mjd/perl/Trace/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you run your program with `perl -d:Trace program', this module will
print a message to standard error just before each line is executed.
This is is something like the shell's `-x' option.

%description -l pl.UTF-8
Jeśli uruchomi się program poprzez `perl -d:Trace program', ten moduł
będzie wypisywał na standardowe wyjście diagnostyczne komunikat przed
wykonaniem każdej linii. Jest to coś w rodzaju opcji `-x' powłoki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__perl} -pi -e 's@<STDIN>;@#<STDIN>;@' test.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Devel/Trace.pm
%{_mandir}/man3/*
