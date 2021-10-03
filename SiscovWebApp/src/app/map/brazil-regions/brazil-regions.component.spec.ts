import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BrazilRegionsComponent } from './brazil-regions.component';

describe('BrazilRegionsComponent', () => {
  let component: BrazilRegionsComponent;
  let fixture: ComponentFixture<BrazilRegionsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BrazilRegionsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BrazilRegionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
