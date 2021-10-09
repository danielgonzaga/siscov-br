import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DistritoFederalComponent } from './distrito-federal.component';

describe('DistritoFederalComponent', () => {
  let component: DistritoFederalComponent;
  let fixture: ComponentFixture<DistritoFederalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DistritoFederalComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DistritoFederalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
