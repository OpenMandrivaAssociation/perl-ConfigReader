%define module   ConfigReader
%define version    0.5
%define release    %mkrel 3

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Read directives from a configuration file
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/ConfigReader/%{module}-%{version}.tar.gz
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*


