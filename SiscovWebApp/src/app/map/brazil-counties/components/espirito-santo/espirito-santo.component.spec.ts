import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EspiritoSantoComponent } from './espirito-santo.component';

describe('EspiritoSantoComponent', () => {
  let component: EspiritoSantoComponent;
  let fixture: ComponentFixture<EspiritoSantoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EspiritoSantoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EspiritoSantoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
