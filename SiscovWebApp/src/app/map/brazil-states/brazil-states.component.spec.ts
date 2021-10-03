import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BrazilStatesComponent } from './brazil-states.component';

describe('BrazilStatesComponent', () => {
  let component: BrazilStatesComponent;
  let fixture: ComponentFixture<BrazilStatesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BrazilStatesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BrazilStatesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
