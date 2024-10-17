%define module   ConfigReader

Name:		perl-%{module}
Version:	0.5
Release:	6
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Read directives from a configuration file
Url:		https://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/ConfigReader/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The ConfigReader::Spec class stores a specification about configuration
directives: their names, whether they are required or if they have default
values, and what parsing function or method to use.

%prep
%setup -q -n %{module}-%{version} 
cat > Makefile.PL <<EOF
use ExtUtils::MakeMaker;

WriteMakefile(
    'NAME'	       => 'ConfigReader::DirectiveStyle',
    'VERSION_FROM' => 'DirectiveStyle.pm',
);
EOF

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.5-3mdv2011.0
+ Revision: 654900
- rebuild for updated spec-helper

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2011.0
+ Revision: 440542
- rebuild

* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-1mdv2009.1
+ Revision: 349954
- import perl-ConfigReader


* Fri Mar 06 2009 cpan2dist 0.5-1mdv
- initial mdv release, generated with cpan2dist

