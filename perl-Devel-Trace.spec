
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Trace
Summary:	Devel::Trace - Print out each line before it is executed (like `sh -x')
Name:		perl-Devel-Trace
Version:	0.10
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	da8d841665fd147b19c4b792fb312da8
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you run your program with `perl -d:Trace program', this module will
print a message to standard error just before each line is executed.
This is is something like the shell's `-x' option.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
perl -pi -e 's@<STDIN>;@#<STDIN>;@' test.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Devel/Trace.pm
%{_mandir}/man3/*
