import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { BrazilRegionsComponent } from './brazil-regions/brazil-regions.component';
import { BrazilStatesComponent } from './brazil-states/brazil-states.component';
import { SharedModule } from '../shared/shared.module';
import { RioDeJaneiroComponent } from './brazil-counties/components/rio-de-janeiro/rio-de-janeiro.component';
import { AcreComponent } from './brazil-counties/components/acre/acre.component';
import { BrazilCountiesComponent } from './brazil-counties/brazil-counties.component';
import { AlagoasComponent } from './brazil-counties/components/alagoas/alagoas.component';
import { AmapaComponent } from './brazil-counties/components/amapa/amapa.component';
import { AmazonasComponent } from './brazil-counties/components/amazonas/amazonas.component';
import { BahiaComponent } from './brazil-counties/components/bahia/bahia.component';
import { CearaComponent } from './brazil-counties/components/ceara/ceara.component';
import { EspiritoSantoComponent } from './brazil-counties/components/espirito-santo/espirito-santo.component';
import { GoiasComponent } from './brazil-counties/components/goias/goias.component';
import { MaranhaoComponent } from './brazil-counties/components/maranhao/maranhao.component';
import { MatoGrossoComponent } from './brazil-counties/components/mato-grosso/mato-grosso.component';
import { MatoGrossoDoSulComponent } from './brazil-counties/components/mato-grosso-do-sul/mato-grosso-do-sul.component';
import { MinasGeraisComponent } from './brazil-counties/components/minas-gerais/minas-gerais.component';
import { ParaComponent } from './brazil-counties/components/para/para.component';
import { ParaibaComponent } from './brazil-counties/components/paraiba/paraiba.component';
import { ParanaComponent } from './brazil-counties/components/parana/parana.component';
import { PernambucoComponent } from './brazil-counties/components/pernambuco/pernambuco.component';
import { PiauiComponent } from './brazil-counties/components/piaui/piaui.component';
import { RioGrandeDoNorteComponent } from './brazil-counties/components/rio-grande-do-norte/rio-grande-do-norte.component';
import { RioGrandeDoSulComponent } from './brazil-counties/components/rio-grande-do-sul/rio-grande-do-sul.component';
import { RondoniaComponent } from './brazil-counties/components/rondonia/rondonia.component';
import { RoraimaComponent } from './brazil-counties/components/roraima/roraima.component';
import { SantaCatarinaComponent } from './brazil-counties/components/santa-catarina/santa-catarina.component';
import { SaoPauloComponent } from './brazil-counties/components/sao-paulo/sao-paulo.component';
import { SergipeComponent } from './brazil-counties/components/sergipe/sergipe.component';
import { TocantinsComponent } from './brazil-counties/components/tocantins/tocantins.component';


@NgModule({
  declarations: [
    BrazilRegionsComponent,
    BrazilStatesComponent,
    BrazilCountiesComponent,
    AcreComponent,
    RioDeJaneiroComponent,
    AlagoasComponent,
    AmapaComponent,
    AmazonasComponent,
    BahiaComponent,
    CearaComponent,
    EspiritoSantoComponent,
    GoiasComponent,
    MaranhaoComponent,
    MatoGrossoComponent,
    MatoGrossoDoSulComponent,
    MinasGeraisComponent,
    ParaComponent,
    ParaibaComponent,
    ParanaComponent,
    PernambucoComponent,
    PiauiComponent,
    RioGrandeDoNorteComponent,
    RioGrandeDoSulComponent,
    RondoniaComponent,
    RoraimaComponent,
    SantaCatarinaComponent,
    SaoPauloComponent,
    SergipeComponent,
    TocantinsComponent,
  ],
  imports: [
    CommonModule,
    SharedModule,
    RouterModule,
    HttpClientModule,
  ],
  exports: [
    BrazilRegionsComponent,
    BrazilStatesComponent,
    BrazilCountiesComponent,
    AcreComponent,
    RioDeJaneiroComponent,
  ]
})
export class MapModule { }
